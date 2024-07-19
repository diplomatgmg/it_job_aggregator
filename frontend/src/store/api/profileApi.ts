import { createApi } from "@reduxjs/toolkit/query/react"
import baseQuery from "@/store/api/baseQuery.ts"
import { HardSkill } from "@/types/hardSkillTypes.ts"
import { Grade } from "@/types/gradeTypes.ts"
import { WorkFormat } from "@/types/workFormatTypes.ts"
import { Profession } from "@/types/professionTypes.ts"
import { Profile, ProfileStatus } from "@/types/profileTypes.ts"
import { PreviewVacancy } from "@/types/vacancyTypes.ts"

const profileApi = createApi({
  reducerPath: "profileApi",
  baseQuery,
  tagTypes: ["Profile"],
  endpoints: (builder) => ({
    getProfileData: builder.query<Profile, void>({
      query: () => "profile/",
    }),
    getProfileStatus: builder.query<ProfileStatus, void>({
      query: () => "profile/is_completed/",
      providesTags: ["Profile"],
    }),
    getProfileVacancies: builder.query<PreviewVacancy[], void>({
      query: () => "profile/vacancies/",
    }),

    setUserHardSkills: builder.mutation<HardSkill[], HardSkill[]>({
      query: (data) => ({
        url: "profile/hard_skills/",
        method: "PATCH",
        body: data,
      }),
      invalidatesTags: ["Profile"],
    }),
    setUserGrades: builder.mutation<Grade[], Grade[]>({
      query: (data) => ({
        url: "profile/grades/",
        method: "PATCH",
        body: data,
        invalidatesTags: ["Profile"],
      }),
    }),
    setUserWorkFormats: builder.mutation<WorkFormat[], WorkFormat[]>({
      query: (data) => ({
        url: "profile/work_formats/",
        method: "PATCH",
        body: data,
        invalidatesTags: ["Profile"],
      }),
    }),
    setUserProfessions: builder.mutation<Profession[], Profession[]>({
      query: (data) => ({
        url: "profile/professions/",
        method: "PATCH",
        body: data,
        invalidatesTags: ["Profile"],
      }),
    }),
  }),
})

export const {
  useGetProfileDataQuery,
  useGetProfileStatusQuery,
  useGetProfileVacanciesQuery,
  useSetUserHardSkillsMutation,
  useSetUserGradesMutation,
  useSetUserWorkFormatsMutation,
  useSetUserProfessionsMutation,
} = profileApi
export default profileApi
