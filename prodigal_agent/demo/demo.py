from prodigal_agent.bus.bus import MessageBus
from prodigal_agent.agents.echo_agent import EchoAgent
from prodigal_agent.agents.user_agent import UserAgent

def main():
    print("\n🚀 Starting Echo Agent Demo...\n")
    
    bus = MessageBus()

    echo = EchoAgent("echo", bus)
    user = UserAgent("user", bus)

    bus.register(echo)
    bus.register(user)

    user.send_message("Hello, Prodigal!", "echo")

if __name__ == "__main__":
    main()
