import Sidebar from "./sidebar"

import { Outlet } from 'react-router-dom'

const Main: React.FC = () => {
     return(
        <div className="home">
            <Sidebar/>
            <main>
                <Outlet/>
            </main>
        </div>
)}
export default Main