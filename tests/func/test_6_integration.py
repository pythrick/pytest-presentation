def list_tasks():
    return ["Buy coffee", "Drink water", "Listen music"]


class TestIntegration:
    def test_add_task(self):
        tasks = list_tasks()
        tasks.append("Buy a new phone")
        assert len(tasks) == 4

    def test_list_tasks(self):
        tasks = ["Buy coffee", "Drink water", "Listen music"]
        assert list_tasks() == tasks
