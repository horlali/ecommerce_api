from django_extensions.management.jobs import MinutelyJob


# class Job(BaseJob):
#     help = "My sample job."

#     def execute(self):
#         print("Hello, World!")

class Job(MinutelyJob):
    help = "Test Job"

    def execute(self):
        print("Hello, World!")