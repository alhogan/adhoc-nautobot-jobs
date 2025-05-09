from nautobot.apps.jobs import Job, StringVar, ChoiceVar

CHOICES = (
    ("-", "----"),
    ("n", "North"),
    ("s", "South"),
)


class Example(Job):
    template_name = "./my_template.html"
    var1 = ChoiceVar(choices=CHOICES, default="-")
    var2 = StringVar()
    var3 = StringVar()

    class Meta:
        name = "Example Job"

    def run(self):
        """Executes the Job."""
        pass
