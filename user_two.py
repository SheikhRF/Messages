from uagents import Agent, Context, Model

class Message(Model):
    message: str

class Message(Model):
    message: str

class Request(Model):
    text: str

class Response(Model):
    text: str
    agent_address: str

DESTINATION = "agent1qd4mdj8rv6zkhf9zu2uhzct95egmzv60tx0q05kgw003983a40585sdttjp"

SEED_PHRASE = "ILoveSendingMessagesToo"

AGENT_MAILBOX_KEY = "3fc55f41-1f70-4bbf-ad06-bf7bb5b2ee5f"

agent = Agent(
    name="user2",
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