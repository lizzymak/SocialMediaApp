import { useState, useEffect } from "react"
import axios from 'axios'

const Home: React.FC = () => {
    const [posts, setPosts] = useState([])
    const user = localStorage.getItem('username')

    type Post = {
        id: number
        image_url: string
        content: string
    }

    const fetchFeed = async()=>{
        try{
            const response = await axios.get(`http://127.0.0.1:8000/feed/${user}`)
            setPosts(response.data)
        }
        catch(err){
            console.log(err)
        }
    }

    useEffect(()=>{
        fetchFeed()
    },[])

    return(
        <div className="homeFeed">
            <h1>Home</h1>
            <div className="postsConatiner">
                    {posts ? (
                        posts.map((post: Post, index: number) => (
                            <div key={index} className="postsCard">
                                {post.image_url && (
                                    <img src={post.image_url} alt="post" />)}
                                    <p>{post.content}</p>
                            </div>
                        ))
                    ):(
                        <h2>No posts...</h2>
                    )}
                </div>
        </div>
        
    )
}

export default Home