from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.answer_generator_agent import AnswerGeneratorAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.template_engine_agent import TemplateEngineAgent

class OrchestratorAgent:
    def run(self, raw_product_data:dict):
        parser=ProductParserAgent()
        q_gen=QuestionGeneratorAgent()
        a_gen=AnswerGeneratorAgent()
        logic_agent=ContentLogicAgent()
        template_engine=TemplateEngineAgent()

        product_model=parser.run(raw_product_data)
        questions=q_gen.run(product_model)
        qa_pairs=a_gen.run(product_model,questions)
        product_b = {
            "name": "RadiantPlus Serum",
            "price": 799,
            "ingredients": ["Hyaluronic Acid"], 
            "benefits": ["Hydration"]
        }
        blocks = logic_agent.run(product_model, product_b)
        
        faq_page=template_engine.generate_faq_page(qa_pairs)
        product_page=template_engine.generate_product_page(product_model,blocks)
        comparison_page= template_engine.generate_comparison_page(product_model,product_b,blocks)
        
        return{
            "faq_page":faq_page,
            "product_page":product_page,
            "comparison_page":comparison_page
        }