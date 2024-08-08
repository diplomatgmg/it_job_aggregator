import { createApi } from "@reduxjs/toolkit/query/react"
import baseQuery from "@/store/api/baseQuery.ts"
import {
  UpdateVacancyViewStatusRequest,
  UpdateVacancyViewStatusResponse,
  UserVacancy,
} from "@/types/vacancyTypes.ts"

const vacancyApi = createApi({
  reducerPath: "vacancyApi",
  baseQuery,
  tagTypes: ["Vacancy"],
  endpoints: (builder) => ({
    getVacancies: builder.query<UserVacancy, void>({
      query: () => "vacancies/",
      providesTags: ["Vacancy"],
    }),
    updateVacancyViewStatus: builder.mutation<
      UpdateVacancyViewStatusResponse,
      UpdateVacancyViewStatusRequest
    >({
      query: (body) => ({
        url: "vacancy/view/",
        method: "POST",
        body,
      }),
      invalidatesTags: ["Vacancy"],
    }),
  }),
})

export const { useGetVacanciesQuery, useUpdateVacancyViewStatusMutation } =
  vacancyApi
export const { invalidateTags } = vacancyApi.util

export default vacancyApi
