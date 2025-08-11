import { useState, useEffect } from "react"
import axios from 'axios'

const Search: React.FC = () => {
    const [userInput, setUserInput] = useState("")
    const [username, setUsername] = useState('')
    const [bio, setBio] = useState('')
    const [profilePic, setProfilePic] = useState('')
    const [posts, setPosts] = useState([])

    const user = localStorage.getItem('username')

    type Post = {
        id: number
        image_url: string
        content: string
    }

    const fetchProfile = async(usernameToFetch: string) => {
        try{
            const response = await axios.get(`http://127.0.0.1:8000/profile/${usernameToFetch}`)
            setUsername(response.data.username)
            setBio(response.data.bio)
            setProfilePic(response.data.profile_pic)
            setPosts(response.data.posts)
            console.log(response)
            }
            catch(err){
            console.log(err)
            }
    }

    const handleSearch = () => {
    if (userInput.trim()) {
        fetchProfile(userInput);
    }
    }

    return(
        <div>
            <h1>Search User</h1>
            <input type="text" onChange={(e)=>setUserInput(e.target.value)}/>
            <button onClick={handleSearch}>+</button>

            {username && userInput.trim() !== "" &&(
                <div className="layout">
            <div className="profile">
                <div>
                    <img src={profilePic || "/images/defaultPFP.jpg"} alt="No profile pic" />
                </div>
                <h1>{username}</h1>
                <h2>{bio}</h2>
            </div>

            <div className="profile">
                <div className="postsTopArea">
                    <h1>Posts</h1>
                </div>
                
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
        </div>

            )}
            
        </div>
        
    )
}

export default Search