from core.message_bus import MessageBus
from core.orchestrator import Orchestrator
from core.task import Task

from agents.product_parser_agent import ProductParserAgent
from agents.question_agent import QuestionAgent
from agents.answer_agent import AnswerAgent
from agents.content_block_agent import ContentBlockAgent
from agents.tamplate_agent import TemplateAgent
from agents.persistence_agent import ArtifactPersistenceAgent
bus =MessageBus()
agents=[]

orchestrator = Orchestrator(bus,agents)

agents.extend([
    ProductParserAgent(),
    QuestionAgent(),
    AnswerAgent(),
    ContentBlockAgent(),
    TemplateAgent(),
    ArtifactPersistenceAgent()

])
raw_product = {
    "Product Name": "GlowBoost Vitamin C Serum",
    "Benefits": "Brightening, Fades dark spots",
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "Key Ingredients": "Vitamin C, Hyaluronic Acid",
    "Price": "₹699"
}
bus.publish(Task("PRODUCT_INPUT_RECEIVED", raw_product))
orchestrator.run()
