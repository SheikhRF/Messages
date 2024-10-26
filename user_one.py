from uagents import Agent, Context, Model

class Message(Model):
    message: str

SEED_PHRASE = "ILoveSendingMessages"
 
# Copy the address shown below

# Now go to https://agentverse.ai, register your agent in the Mailroom by providing the address you just copied.
# Then, copy the agent's mailbox key and insert it here below inline
AGENT_MAILBOX_KEY = "4f598b12-d856-4f59-ae72-b7409396960f"  # "3fc55f41-1f70-4bbf-ad06-bf7bb5b2ee5f"

# Now your agent is ready to join the agentverse!
agent = Agent(
    name="user1",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

# print(agent.address) agent1qd4mdj8rv6zkhf9zu2uhzct95egmzv60tx0q05kgw003983a40585sdttjp

@agent.on_event("startup")
async def initialise(ctx: Context):
    await ctx.send("agent1q02jy3kk437pywwnjdrdqux44xksq9cg47n9gmwyu0ezegp0u5r675xkqre", Message(message="test"))

@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    agent.run()