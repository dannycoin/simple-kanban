import Board from './components/Board';
import { DndProvider } from 'react-dnd'
import { HTML5Backend } from 'react-dnd-html5-backend'
import './App.css'

const App = () => {

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="app">
        <h1>Tablero Simple Kanban</h1>
        <Board />
        <div className="footer">
          <span>Simple Kanban v1.0</span>
          <span>Mambo Admisión | Danny Prats (c) 2024</span>
        </div>
      </div>
    </DndProvider>
  );
};

export default App;