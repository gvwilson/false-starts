"""Create our own exceptions."""


class NitinatException(Exception):
    """Something went wrong in the Nitinat package."""

    def __init__(self, msg=""):
        """Remember what went wrong."""
        self.msg = msg

    def __repr__(self):
        """Printable."""
        msg = self.msg if self.msg else "-no message-"
        return f"<exc {msg}>"
