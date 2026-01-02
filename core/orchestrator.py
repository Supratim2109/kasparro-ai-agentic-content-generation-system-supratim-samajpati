class Orchestrator:
    def __init__(self,bus,agents):
        self.bus=bus
        self.agents=agents
        self.artifact= {}

    def run(self):
        while self.bus.has_tasks():
            task=self.bus.next_task()

            for agent in self.agents:
                if agent.can_handle(task):
                    new_tasks=agent.handle(task)

                    for t in new_tasks:
                        self.bus.publish(t)

            if self._done():
                break

    def _done(self):
        return (
            "faq_page" in self.artifact and
            "product_page" in self.artifact and
            "comparison_page" in self.artifact
        )