import { useState } from "react"
import axios from 'axios'
import { useNavigate } from "react-router-dom" 

const Login: React.FC = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [isRegistering, setIsRegistering] = useState(false)
    const navigate = useNavigate()

    const handleLogin = async(e: React.FormEvent) => {
        e.preventDefault()
        const endpoint = isRegistering ? 'register' : 'login'
        const data = isRegistering ? {username, email, password} : {username, password}
        try{
            const response = await axios.post(`http://127.0.0.1:8000/${endpoint}`, data)
            const token = response.data.token
            localStorage.setItem('token', token)
            navigate("/main")
            console.log('login successful')
    }
        catch(err: any){
            console.log('Login fail', err)
        }
    }


    return (
        <div className="login">
        <h2>{isRegistering ? 'Register' : 'Login'}</h2>
        <form onSubmit={handleLogin}>
            {isRegistering === true && (
                <input type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="email" />
            )}
            
            <input type="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="username" 
            />

            <input type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="password" 
            />

            <button type="submit">login</button>
        </form>
        <p className='changeLogin' onClick={() => setIsRegistering(!isRegistering)}>
            {isRegistering ? 'Already have an account? Login' : "Don't have an account? Register"}
        </p>
        </div>
    )  
}

export default Login