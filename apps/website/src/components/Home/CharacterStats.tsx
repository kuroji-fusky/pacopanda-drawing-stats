import { CharacterCard } from "@components/Cards"

import s from "./Section.module.scss"

export function CharacterStats() {
  return (
    <section className={s["wrapper"]}>
      <CharacterCard />
      <CharacterCard />
      <CharacterCard />
      <CharacterCard />
      <CharacterCard />
      <CharacterCard />
    </section>
  )
}
