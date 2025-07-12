// Author: Kim Sang Huynh
// ISU Netid: step1994@iastate.edu
// Date: March 28th, 2025

import { UserCard } from './step1994_Activity09_Modules_Components_Props_UserCard';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (
    <>
      <UserCard
        picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFDcwrn-ojY65XbXItgoxDwzrEJydFPu_ocw&s"
        name="Mark Zuckerberg"
        salary={3000}
        status={true}
        address={{
          street: "123 Bellmont Rd.",
          city: "San Francisco",
          state: "California"
        }}
      />
      
      <UserCard
        picture="https://shifters.tech/wp-content/uploads/2020/12/Microsoft.jpg"
        name="Bill Gates"
        salary={10000}
        status={true}
        address={{
          street: "456 Montbell Rd.",
          city: "Seattle",
          state: "Washington"
        }}
      />
    </>
  );
}

export default App;