def test_message_copy_with_new_content():
    from MultiProdigy.schemas.message import Message

    msg = Message(sender="a", receiver="b", content="hello")
    new_msg = msg.copy_with_new_content("hi")

    assert new_msg.content == "hi"
    assert new_msg.sender == msg.sender
    assert new_msg.metadata == msg.metadata
