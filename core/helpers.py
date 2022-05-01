BASE_PATH = "core/notes/"


def getPath(ctx):
    return BASE_PATH + str(ctx.guild.id) + ".txt"