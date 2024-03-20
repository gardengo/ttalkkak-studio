import styled from 'styled-components'

interface MineTabStyleProp {
  $showMode: boolean
}

interface ShowMineTabProp {
  showMine: boolean
  handleMineChange: (target: boolean) => void
}

const MineTabWrapper = styled.div`
  display: flex;
  width: 80%;
`

const MineTab = styled.div<MineTabStyleProp>`
  border-bottom: solid ${(props) => (props.$showMode ? 'black' : 'white')};
  flex: 1;
  text-align: center;
  padding: 10px;
`

function ShowMineTab({ showMine, handleMineChange }: ShowMineTabProp) {
  return (
    <MineTabWrapper>
      <MineTab $showMode={!showMine} onClick={() => handleMineChange(false)}>
        전체
      </MineTab>
      <MineTab $showMode={showMine} onClick={() => handleMineChange(true)}>
        구매한 상품
      </MineTab>
    </MineTabWrapper>
  )
}

export default ShowMineTab
