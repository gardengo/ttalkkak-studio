'use client'

import { useState, useEffect } from 'react'

function StartPage() {
  const [device, setDevice] = useState<string | null>(null)

  function renderMessage() {
    if (device === 'web') {
      return <p>모바일 환경에서 접속해 주세요</p>
    } else if (device === 'android' || device === 'iphone') {
      return <button>시작하기</button>
    }
  }

  useEffect(() => {
    const agent = navigator.userAgent
    let tempDevice = 'web'

    if (agent.toLowerCase().indexOf('android') >= 0) {
      tempDevice = 'android'
    } else if (agent.toLowerCase().indexOf('iphone') >= 0) {
      tempDevice = 'iphone'
    }

    setDevice(tempDevice)
  }, [device])

  return (
    <main>
      <h1>스타트 페이지</h1>
      {renderMessage()}
    </main>
  )
}

export default StartPage