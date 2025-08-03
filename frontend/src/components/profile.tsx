import { useState, useEffect } from "react"
import axios from 'axios'
import { useNavigate } from "react-router-dom" 

const Profile: React.FC = () => {
    const [username, setUsername] = useState('')
    const [bio, setBio] = useState('')
    const [profilePic, setProfilePic] = useState('')
    const [editMode, setEditMode] = useState(false)
    const [editProfile, setEditProfile] = useState({ username: "", bio: "", profile_pic: "" })
    const user = localStorage.getItem('username')

    const fetchProfile = async () => { //this gets users profile data and sets it
            try{
            const response = await axios.get(`http://127.0.0.1:8000/profile/${user}`)
            setUsername(response.data.username)
            setBio(response.data.bio)
            setProfilePic(response.data.profile_pic)
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
                    <input type="text" placeholder="type new bio..." onChange={(e) => setEditProfile({ ...editProfile, bio: e.target.value })}/>
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
                    <button>+</button>
                </div>
                
            </div>
        </div>
    )
}

export default Profile