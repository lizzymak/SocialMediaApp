import { useState, useEffect } from "react"
import axios from 'axios'
// import { useNavigate } from "react-router-dom" 
// import path from "path"

const Profile: React.FC = () => {
    const [username, setUsername] = useState('')
    const [bio, setBio] = useState('')
    const [profilePic, setProfilePic] = useState('')
    const [posts, setPosts] = useState([])
    const [editMode, setEditMode] = useState(false)
    const [editProfile, setEditProfile] = useState({ username: "", bio: "", profile_pic: "" })
    const user = localStorage.getItem('username')

    const [showModal, setShowModal] = useState(false)
    const [postText, setPostText] = useState<string | "">("")
    const [postPic, setPostPic] = useState<string | null>(null)

    type Post = {
        id: number
        image_url: string
        content: string
    }

    const fetchProfile = async () => { //this gets users profile data and sets it
            try{
            const response = await axios.get(`http://127.0.0.1:8000/profile/${user}`)
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
    
    useEffect(() =>{ //runs once after first render
        fetchProfile()
    },[])


    const save = async() => { //updates users profile info in db and rerenders 
        try{
            await axios.patch(`http://127.0.0.1:8000/profile/${user}`,{
                username: editProfile.username,
                bio: editProfile.bio,
                profile_pic: editProfile.profile_pic
            })
            alert('profile updated')
            fetchProfile()
            setEditMode(false)
        }
        catch{
            alert("profile update failed")
        }
    }

    const createPost = async() => {
        try{
            const res = await axios.post(`http://127.0.0.1:8000/profile/post/${user}`,{
                content: postText,
                image_url: postPic 
            })
            setShowModal(false)
            setPostPic(null)
            setPostText("")
            fetchProfile()
            return res.data
        }
        catch{
            alert("create post failed")
        }
    }

    const profilePicChange = (e: React.ChangeEvent<HTMLInputElement>) => { //reads file and converts to base64 encoded img
        const file = e.target.files?.[0]
        if(file){
            const reader = new FileReader()
            reader.onloadend = () => {
                // reader.result can be string, ArrayBuffer, or null
            if (typeof reader.result === "string") {
                setEditProfile({ ...editProfile, profile_pic: reader.result });
            }
        }
        reader.readAsDataURL(file)
    }
}

const postImageChange = (e: React.ChangeEvent<HTMLInputElement>) => { //reads file and converts to base64 encoded img
        const file = e.target.files?.[0]
        if(file){
            const reader = new FileReader()
            reader.onloadend = () => {
                // reader.result can be string, ArrayBuffer, or null
            if (typeof reader.result === "string") {
                setPostPic(reader.result)
            }
        }
        reader.readAsDataURL(file)
    }
}



    

    return(
        <div className="layout">
            <div className="profile">
                
                <div>
                    <img src={profilePic || "/images/defaultPFP.jpg"} alt="No profile pic" />
                    {editMode && (
                        <input type="file" accept="image/*" onChange={profilePicChange}/>
                    )}
                </div>
                <h1>{username}</h1>
                {editMode ? (
                    <input type="text" placeholder="type new bio..." className="bioInput" onChange={(e) => setEditProfile({ ...editProfile, bio: e.target.value })}/>
                ):(
                    <h2>{bio}</h2>
                )}
                {!editMode ? (
                    <button onClick={()=>setEditMode(true)}>Edit Profile</button>
                ):(
                    <div>
                        <button onClick={save}>Save</button>
                        <button onClick={()=>setEditMode(false)}>Cancel</button>
                    </div>
                )}
                
            </div>
            <div className="profile">
                <div className="postsTopArea">
                    <h1>Posts</h1>
                    <button onClick={()=>setShowModal(true)}>+</button>
                </div>
                {showModal && (
                    <div className="modal">
                        <div className="content">
                            <h2>Create Post</h2>
                            {postPic && (<img src={postPic} alt="preview" className=""/>)}
                            <input type="file" onChange={postImageChange}/>
                            
                            <textarea placeholder= 'Write something...' value={postText} onChange={(e)=>setPostText(e.target.value)}></textarea>
                            <button type="submit" onClick={createPost}>Post</button>
                            <button onClick={()=>setShowModal(false)} >Cancel</button>
                        </div>
                    </div>
                )}
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
    )
}

export default Profile