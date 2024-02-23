from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table
from rich.prompt import Prompt
from rich.console import Console



class LiveProgress:
    def __init__(self, n_tests=2, use_case="check"):
        self.n_tests = n_tests
        self.current_test_number = 1

        self.message_tests_passed = {"check": "Тестов пройдено", "stage": "Тестов сгенерировано"}[use_case]
        self.message_all_tests_passed = {"check": "Все тесты пройдены", "stage": "Все тесты сгенерированы"}[use_case]

        self.job_progress = Progress(
            "[{task.fields[caption_color]}]{task.description}",
            BarColumn(bar_width=25, pulse_style="green3", complete_style="green3", finished_style="green3"),
            TextColumn("[progress.percentage][{task.fields[display_color]}]{task.percentage:>3.0f}%"),
            redirect_stdout=False,
            redirect_stderr=False
        )
        self.jobs = [
            self.job_progress.add_task("Предпроверка решения", total=1, display_color="green3", caption_color="blue"),
            self.job_progress.add_task("Подготовка данных", total=1, display_color="green3", caption_color="blue"),
            self.job_progress.add_task("Запуск решения", total=1, display_color="green3", caption_color="blue"),
            self.job_progress.add_task("Проверка ответа", total=1, display_color="green3", caption_color="blue"),
            self.job_progress.add_task("Очистка окружения", total=1, display_color="green3", caption_color="blue")
        ]

        self.overall_progress = Progress(
            "[b][{task.fields[caption_color]}]{task.description}",
            BarColumn(bar_width=25, complete_style="green3", finished_style="green3"),
            TextColumn("[{task.fields[caption_color]}]{task.completed}/{task.total}"),
            redirect_stdout=False,
            redirect_stderr=False
        )

        self.overall_task = self.overall_progress.add_task(self.message_tests_passed, total=self.n_tests, caption_color="blue")

        self.overall_panel = Panel.fit(
            self.overall_progress, title="Общий прогресс", border_style="blue", padding=(3, 2, 3, 2)
        )

        self.test_panel = Panel.fit(self.job_progress, title="Текущий тест", border_style="blue", padding=(1, 2))

        self.progress_table = Table.grid()
        self.progress_table.add_row(self.overall_panel, self.test_panel)
    

    def __enter__(self):
        self.live = Live(self.progress_table, refresh_per_second=10)
        self.live.__enter__()
        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.live.__exit__(exc_type, exc_val, exc_tb)
    

    def start_test(self):
        # self.live.console.print(f"[green3]Запускаю тест #{self.current_test_number}...")
        self.test_panel.title = f"Текущий тест: {self.current_test_number}"
        for job in self.jobs:
            self.job_progress.reset(job, start=True, total=1)
    

    def complete_test(self):
        self.overall_progress.advance(self.overall_task)
        self.current_test_number += 1
        if self.current_test_number > self.n_tests:
            self.test_panel.title = f"[green3]✓ {self.message_all_tests_passed}"

    
    def start_job_idx(self, idx):
        self.job_progress.reset(self.jobs[idx], start=False, total=None)
    
    def complete_job_idx(self, idx):
        self.job_progress.reset(self.jobs[idx], total=1, completed=1)
    
    def fail_job_idx(self, idx):
        self.live.console.print(f"[red][bold]ОШИБКА[/bold] Тест {self.current_test_number} не пройден.")
        self.job_progress.reset(self.jobs[idx], display_color="red", caption_color="red")
        self.overall_panel.border_style = "red"
        self.test_panel.border_style = "red"
        self.test_panel.title = f"Тест {self.current_test_number} - [b]ОШИБКА"
        self.overall_progress.update(self.overall_task, caption_color="red")
    
    @property
    def failed(self):
        return self.failed_job_idx is not None
    
    def get_error_text(self):
        return self.error_text



def display_error(error_text):
    if len(error_text) < 240 and len(error_text.split("\n")) <= 3:
        console = Console()
        console.print("[red]" + error_text)
        return

    display_error = Prompt.ask("[blue]Показать детальную информацию об ошибке?", choices=["y", "n"], default="y")
    if display_error == "y":
        console = Console()
        with console.pager():
            console.print(error_text)



def display_ok(ok_text):
    console = Console()
    console.print(f"[green3] ✓ {ok_text}")
    console.print()