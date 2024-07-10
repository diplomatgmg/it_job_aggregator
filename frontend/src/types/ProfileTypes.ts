import { HardSkill } from "@/types/hardSkillTypes.ts"
import { Grade } from "@/types/gradeTypes.ts"
import { WorkFormat } from "@/types/workFormatTypes.ts"
import { Profession } from "@/types/professionTypes.ts"

export interface Profile {
  isCompleted: boolean
  hardSkills: HardSkill[]
  grades: Grade[]
  workFormats: WorkFormat[]
  profession: Profession[]
}
