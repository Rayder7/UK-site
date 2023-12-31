import React from  "react"
import './New.css'
import { New } from "../../models"
import newobject from  "../../static/img/newsobject.png"
import { NavLink } from "react-router-dom";

interface NewsProps {
    news: New
}

export function NewObject({news}: NewsProps) {
    return (
        <div className="container-news-object">
          <div className="container-news-left">
            <img src={newobject} alt="новость" />
          </div>
          <div className='containter-news-right'>
            <div className='news-column-created-date'>
              {news.created_date} 
            </div>
            <div className='news-column-title'>
              <NavLink to='/' className='nav-link'>{news.title}</NavLink>
            </div>
            <div className='news-column-text'>
              {news.text} 
            </div>
          </div>
        </div>
    )
}