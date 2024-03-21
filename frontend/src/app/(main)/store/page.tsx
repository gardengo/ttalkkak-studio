'use client'

import styled from 'styled-components'
import { ChangeEvent, useState } from 'react'
import OptionList from './_components/OptionList'
import CategoryList from './_components/CategoryList'
import ShowMineTab from './_components/ShowMineTab'

const MainContainer = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
`

const ContentContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 1440px;
`

function StorePage() {
  const [showMine, setShowMine] = useState<boolean>(false)
  const [categorySort, setCategorySort] = useState<number>(0)

  function handleCategoryChange(event: ChangeEvent<HTMLSelectElement>) {
    setCategorySort(Number(event.target.value))
  }

  function handleMineChange(stat: boolean) {
    setShowMine(stat)
  }

  return (
    <MainContainer>
      <h1>옵션 스토어</h1>
      <ContentContainer>
        <ShowMineTab showMine={showMine} handleMineChange={handleMineChange} />
        <CategoryList
          categorySort={categorySort}
          handleCategoryChange={handleCategoryChange}
        />
        <OptionList categorySort={categorySort} showMine={showMine} />
      </ContentContainer>
    </MainContainer>
  )
}

export default StorePage