import React from 'react'
import './Footer.css'
import { AiFillPhone, AiOutlineMail } from "react-icons/ai";


export function Footer() {
  return (
    <div className='footer'>
        <div className='info'>
            <div className='phonenumber'>
                <div className='info-column'><AiFillPhone/></div>
                <div className='info-column'><h2>+7 (351) xxx-xx-xx</h2></div>
            </div>
            <div className='email'>
                <div className='info-column'><AiOutlineMail/></div>
                <div className='info-column'><h2>UK-site@gmail.com</h2></div>
            </div>
        </div>
        <div className='info-site'>
           <h4>2023 ООО "Управляющая комания"</h4>
           <h5>Любая информация, представленная на данном сайте, носит исключительно информационный характер и не является публичной офертой.</h5>
        </div>

    </div>
  )
}