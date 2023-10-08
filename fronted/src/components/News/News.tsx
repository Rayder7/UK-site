import React from  "react"
import './News.css'
import { New } from "../../models"

interface NewsProps {
    news: New
}

export function NewsList({news}: NewsProps) {
    return (
        <div className="container-result">
          <div className="container-left">
            <>{news.title} </>
            <>{news.text} </>
            <>{news.created_date} </>

          </div>
        </div>
    )
}