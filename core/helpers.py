BASE_PATH = "core/"


def getPath(ctx):
    return BASE_PATH + str(ctx.guild.id) + ".txt"