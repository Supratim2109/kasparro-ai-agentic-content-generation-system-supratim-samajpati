**1. Problem Statement**



The objective of this project is to design and implement a modular, agentic automation system that transforms a small, structured product dataset into multiple machine-readable content pages such as FAQs, product descriptions, and comparisons.



The system must demonstrate:



* True multi-agent architecture
* Autonomous agents with clear responsibilities
* Dynamic coordination without static or hard-coded control flow
* Reusable content logic and template-based generation
* Fully structured JSON outputs suitable for downstream systems





**2. Solution Overview**



This project implements a task-driven, event-based multi-agent system where independent agents collaborate through a shared task bus to progressively transform raw product data into structured content artifacts.



Key characteristics of the solution:



* Agents do not call each other directly
* Execution order is not predefined
* Coordination emerges dynamically based on task availability
* Each agent decides autonomously whether it can act on a given task
* The orchestrator manages lifecycle only, not business logic



The system produces three final outputs:



* FAQ Page (faq.json)
* Product Description Page (product\_page.json)
* Comparison Page (comparison\_page.json)



All outputs are strictly machine-readable JSON.



**3. Scope \& Assumptions**

In Scope



* Rule-based content generation using structured product data
* Deterministic behavior without external APIs or LLMs
* Single product input with a fictional comparison product
* Local JSON persistence as final artifacts
* Autonomous agent coordination via message passing



Out of Scope



* Natural language creativity or copywriting quality
* UI rendering or frontend concerns
* External data sources or real-time APIs
* Prompt engineering or generative AI usage



Assumptions



* Product input is provided as a key-value structure
* Agents may maintain local internal state but no shared global state
* Task names are treated as system-level contracts
* The system runs synchronously in a single process for simplicity



**4. System Design** 

**4.1 Architectural Style**



The system follows a task-driven agentic architecture, inspired by event-driven systems and autonomous agent models.



Core principles:



* Tasks represent system state transitions, not function calls
* Agents subscribe to task types, not execution order
* Autonomy is achieved through capability checks, not central control
* Coordination emerges dynamically through shared tasks



**4.2 Core Components**

**1. Task**



A task is a lightweight message representing a state change or requirement in the system.



Each task contains:



* type: semantic identifier (e.g., PRODUCT\_NORMALIZED)
* payload: structured data relevant to the task



Tasks are immutable once created.



**2. Message Bus**



The message bus is a shared infrastructure component responsible for:



* Storing pending tasks
* Allowing tasks to be published and consumed



It contains no business logic and has no knowledge of agents.



**3. Orchestrator**



The orchestrator is not an agent.



Its responsibilities are limited to:



* Initializing the system
* Dispatching tasks from the message bus
* Offering each task to all registered agents
* Managing system termination conditions



The orchestrator:



* Does not know agent order
* Does not enforce workflow steps
* Does not contain transformation logic



**4.3 Agent Model**



All agents implement a common contract:



* can\_handle(task) → bool
* handle(task) → list\[Task]



Agents are autonomous and:



* Decide whether they can act on a task
* May emit zero or more new tasks
* Never call other agents directly



**4.4 Agent Responsibilities**



**Product Parser Agent**



* Reacts to raw product input
* Normalizes arbitrary key-value data into a clean internal model
* Emits PRODUCT\_NORMALIZED



**Question Generator Agent**



* Reacts to normalized product data
* Uses a rule-based expert system to generate 15 categorized questions
* Emits QUESTIONS\_GENERATED



**Answer Generator Agent**



* Reacts to generated questions
* Produces deterministic, category-aware answers
* Emits QA\_GENERATED



**Content Block Agent**



* Aggregates product data and Q\&A data over time
* Maintains local state to ensure completeness
* Emits CONTENT\_BLOCKS\_READY only when all required blocks are available
* This agent is critical for decoupling execution order from data readiness.



Template Agent



* Reacts to complete content blocks
* Applies structured templates for:

&nbsp;	1. FAQ Page

&nbsp;	2. Product Page

&nbsp;	3. Comparison Page

* Emits PAGE\_GENERATED tasks



Templates are defined as independent, reusable schema functions.



**Artifact Persistence Agent**



* Reacts to PAGE\_GENERATED
* Writes structured JSON files to disk
* Produces no downstream tasks



Persistence is treated as a side-effect agent, not a workflow step.



**4.5 Dynamic Coordination**



Execution order emerges as follows:



* A task appears in the message bus
* All agents independently evaluate whether they can act
* Capable agents emit new tasks
* The system progresses until no tasks remain



**5 Flow Diagram**



PRODUCT\_INPUT\_RECEIVED

&nbsp;       ↓

PRODUCT\_NORMALIZED

&nbsp;       ↓

QUESTIONS\_GENERATED

&nbsp;       ↓

QA\_GENERATED

&nbsp;       ↓

CONTENT\_BLOCKS\_READY

&nbsp;       ↓

PAGE\_GENERATED

&nbsp;       ↓

JSON FILES



