from uagents import Agent, Context, Model
from flask import Flask
from time import sleep
from requests import post, get
import json

DESTINATION = "agent1q02jy3kk437pywwnjdrdqux44xksq9cg47n9gmwyu0ezegp0u5r675xkqre"
SEED_PHRASE = "ILoveSendingMessages"
AGENT_MAILBOX_KEY = "4f598b12-d856-4f59-ae72-b7409396960f"

app = Flask(__name__)

class Message(Model):
    message: str

class Request(Model):
    text: str

class Response(Model):
    text: str
    agent_address: str

agent = Agent(
    name="user1",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

received_messages = []

@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    received_messages.append(msg.message)  # Store the incoming message

@agent.on_rest_post("/rest/post", Request, Response)
async def handle_post(ctx: Context, req: Request) -> Response:
    ctx.logger.info("Received POST request")
    await ctx.send(DESTINATION, Message(message=req.text))
    return Response(text="Message sent", agent_address=DESTINATION)

# Endpoint to retrieve messages
@agent.on_rest_get("/rest/get_messages", Response)
async def get_messages(ctx: Context):
    # Return the list of received messages as a JSON response
    print(received_messages)
    return json.dumps(str(received_messages))

if __name__ == "__main__":
    agent.run()
