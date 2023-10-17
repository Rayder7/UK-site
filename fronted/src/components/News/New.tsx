import React from  "react"
import './New.css'
import { New } from "../../models"
import newobject from  "../../static/img/newsobject.jpg"

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
              {news.title} 
            </div>
            <div className='news-column-text'>
              {news.text} 
            </div>
          </div>
        </div>
    )
}