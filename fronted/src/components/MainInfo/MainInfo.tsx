import React from 'react'
import './MainInfo.css'



export function MainInfo() {
  return (
    <div className='maininfo'>
      <div className='container-maininfo-with-photo'>
        <div className="maininfo-text-in-photo">
            <h2>Добро пожаловать на сайт<br/>
                управляющей организации<br/>
                «Uk-site»
            </h2>
            </div>
        </div>
      <div className='container-maininfo-links-board'>
        links
      </div>
      <div className='container-maininfo-info-board'>
        <div className='info-board'>
            <div className='info-board-img'>
                <img src={"https://avatars.mds.yandex.net/i?id=1496e6f3baefc101d096e9df34471c89d17e3d06-9859478-images-thumbs&n=13"}
                    width="300" height="300"/>
            </div>
            <div className='info-board-text-1'>
                <h2>Комфорт проживания</h2>
                <h3>Современные инженерно-технические системы, просторные благоустроенные дворы, поддержание бесперебойной работы 24/7.</h3>
            </div>
        </div>
        <div className='info-board'>
            <div className='info-board-text-2'>
                <h2>Оперативность</h2>
                <h3>Единый контакт центр, штат специалистов и профессионалов своего дела позволяют максимально оперативно реагировать на заявки собственников.</h3>
            </div>
            <div className='info-board-img'>
                <img src={"https://avatars.mds.yandex.net/i?id=1496e6f3baefc101d096e9df34471c89d17e3d06-9859478-images-thumbs&n=13"}
                    width="300" height="300"/>
            </div>
        </div>
      </div>
    </div>
  )
}