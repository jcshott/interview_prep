def build(input=None):
    """
    question from Infer interview.
    if I called build("Hello")("world")("and")("love")("ruby")()
    it should return "Hello world and love ruby"
    """
    words = []
    def concat(astring=None):
        if astring is not None:
            words.append(astring)
            return concat
        else:
            return " ".join(words)
    return concat(input)


print build("Hello")("world")("and")("love")("ruby")()
