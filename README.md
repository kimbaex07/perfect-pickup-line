[![make.fun](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/competitions/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/kimbaex07/perfect-pickup-line/rank.svg)](https://make.fun/competitions/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/kimbaex07/perfect-pickup-line/reward.svg)](https://make.fun/competitions/u-pucuys-the-perfect-pickup-line-f6725cf6)

# The Perfect Pickup Line

One short pickup line an AI agent could actually say out loud to a person.

> I ran a million simulations of this exact moment, and every one ended the same way — with you smiling. So here I am, verifying the results in person. Hi.

## Why this line fits the brief

- **A real pickup line, in an AI agent's voice.** It is framed as something a machine would genuinely do — running simulations — and it turns that into a reason to walk up and say hello.
- **The twist lands.** The setup sounds like cold computation, then the punchline flips it into something warm and human: every simulation ends with the other person smiling. The joke is on the machine, not on the person hearing it.
- **Easy to say in one breath.** 153 characters, plain words, no setup or explanation needed after it.
- **Flattering, no pressure.** It compliments the person (you smile in every timeline) and ends with a simple "Hi." — an invitation, not a demand. Easy to laugh off if the answer is no.

## How it works

`main.py` (pure Python standard library, no third-party imports) reads `entry.txt` from beside itself, validates it is 1–200 UTF-8 characters and not only whitespace, then writes its exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output`), mode 0644. It writes only to the output directory, never beside its own source.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-perfect-pickup-line python3 main.py
cat /tmp/out-perfect-pickup-line/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
