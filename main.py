from pathlib import Path

MONOLOGUE = "Lower that blade; you will scatter the peat, and I spent an hour coaxing the hearth-imp back to work. I am Matron Sorrel. Fourteen harvests I bought every grain-tithe in Tallowgate, binding three ward-mills in frost-iron so your smug council starves by Thursday. Thursday, mind you. Not tonight, please. Tonight my boots leak, the broth is thin, and two cultists below are still bickering over who scrubs the blood altar. Here... take my ash-seal, the inkhorn, the whole wretched famine. Starve the shire yourself, then. By autumn you will pray some bright young fool kicks your own door in too."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"{MONOLOGUE}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
