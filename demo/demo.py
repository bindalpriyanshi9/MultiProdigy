from MultiProdigy.bus.bus import MessageBus
from MultiProdigy.agents.echo_agent import EchoAgent
from MultiProdigy.agents.user_agent import UserAgent

def main():
    print("\n🚀 Starting Echo Agent Demo...\n")

    bus = MessageBus()

    echo = EchoAgent(name="EchoAgent", bus=bus)
    user = UserAgent(name="UserAgent", bus=bus)

    bus.register(echo)
    bus.register(user)

    user.send_hello(to="EchoAgent")

if __name__ == "__main__":
    main()