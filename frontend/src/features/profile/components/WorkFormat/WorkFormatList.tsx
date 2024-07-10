import SelectableList from "@/features/profile/components/Selectable/SelectableList.tsx"
import { FC } from "react"
import { WorkFormat } from "@/types/workFormatTypes.ts"
import { useSetUserWorkFormatsMutation } from "@/store/api/profileApi.ts"

interface WorkFormatListProps {
  workFormats: WorkFormat[]
  userWorkFormats: WorkFormat[]
}

const WorkFormatList: FC<WorkFormatListProps> = ({
  workFormats,
  userWorkFormats,
}) => (
  <SelectableList
    items={workFormats}
    userItems={userWorkFormats}
    mutation={useSetUserWorkFormatsMutation}
  />
)

export default WorkFormatList