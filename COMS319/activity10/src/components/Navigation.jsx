import logo from '../assets/isu_logo.png';
import Categories from '../data/Categories';

const Navigation = ({ onTagClick }) => {
  return (
    <div className='fixed top-0 left-0 w-[300px] h-screen bg-blue-950 p-6 text-white flex flex-col items-center'>
      <img src={logo} alt='logo' className='pt-20 mb-3 w-full'/>
      <h1 className='text-3xl font-extrabold mb-4'>Product Catalog</h1>
      <button onClick={() => onTagClick('all')} className='bg-amber-500 px-4 py-2 rounded-full text-black hover:bg-black hover:text-white mb-2'>All</button>
      {Categories.map(tag => (
        <button key={tag} onClick={() => onTagClick(tag)} className='bg-amber-500 px-4 py-2 m-1 rounded-full text-black hover:bg-black hover:text-white'>
          {tag}
        </button>
      ))}
    </div>
  );
};

export default Navigation;
