import s from "./CharacterCard.module.scss"

interface CharacterCardProps {
  title?: string
  species?: string
  appearances?: string
  image?: string
}

export function CharacterCard(props: CharacterCardProps) {
  return (
    <div className={s["wrapper"]}>
      <div className={s["img-wrapper"]}></div>
      <div className={s["flex-wrapper"]}>
        <div className={s["heading"]}>
        <h2>Name</h2>
        <span className={s["species-chip"]}>Species</span>
        </div>
        <div>No. of appearances</div>
      </div>
    </div>
  )
}
