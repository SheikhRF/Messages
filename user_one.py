from uagents import Agent, Context, Model
from time import sleep

class Message(Model):
    message: str

class Request(Model):
    text: str

class Response(Model):
    text: str
    agent_address: str

DESTINATION = "agent1q02jy3kk437pywwnjdrdqux44xksq9cg47n9gmwyu0ezegp0u5r675xkqre"
SEED_PHRASE = "ILoveSendingMessages"
AGENT_MAILBOX_KEY = "4f598b12-d856-4f59-ae72-b7409396960f"

agent = Agent(
    name="user1",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

@agent.on_rest_post("/rest/post", Request, Response)
async def handle_post(ctx: Context, req: Request) -> Response:
    ctx.logger.info("Received POST request")
    await ctx.send(DESTINATION, Message(message=req.text))

if __name__ == "__main__":
    agent.run()