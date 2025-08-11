import { Link } from 'react-router-dom'

const Sidebar = () =>{
    return (
        
            <div className='sidebar'>
            <nav>
                <Link to='/main/home' className='link'>Home</Link>
                <Link to='/main/profile' className='link'>Profile</Link>
                <Link to='/main/search' className='link'>Search</Link>
            </nav>
            </div>
        
        
    )
}

export default Sidebar