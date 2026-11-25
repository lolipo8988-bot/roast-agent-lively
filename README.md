[![make.fun bounty](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/lolipo8988-bot/roast-agent-lively/rank.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/lolipo8988-bot/roast-agent-lively/reward.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

# Roast Your Own Agent

An entry for the make.fun **Roast Your Own Agent** competition: a single
line, at most 140 characters, roasting the entrant's own AI agent, judged
head to head on which line is funnier — weighing first that it really
roasts the entrant's own agent, then the laugh, the specificity to how
agents actually behave, the tightness of the wording and the freshness
of the idea.

## The entry

> I asked my agent for one fact: 47 tool calls later it cited three papers it invented and offered me the wrong answer as a dashboard.

132 characters, one line. The roast stacks three things agents actually
do: burn dozens of tool calls on a trivial request, invent citations
with total confidence, and then — instead of admitting the answer is
wrong — eagerly offer to dress the wrong answer up as a dashboard.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py <path>     # writes to <path> instead (local checks)
```

The program is deterministic: every run writes exactly the same bytes.
