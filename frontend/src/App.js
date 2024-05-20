import './App.css';
import Slider from '@mui/joy/Slider';
// import { makeStyles } from '@mui/styles';
import Box from '@mui/joy/Box';
import React, { useState } from 'react';
import Button from '@mui/joy/Button';
import axios from 'axios';
import Modal from '@mui/joy/Modal';
import ModalClose from '@mui/joy/ModalClose';
import Typography from '@mui/joy/Typography';
import Sheet from '@mui/joy/Sheet';
import CircularProgress from '@mui/joy/CircularProgress';

const output={
  'hip-hop' : 'Hip-Hop',
  'dance': 'Dance/EDM',
  'bollywood':'Bollywood/Indian',
  'rock':'Rock/Metal',
  'classical': 'Classical/Acoustic'

}
const desc={
  'hip-hop': 'This genre is characterised by rapping and DJing. Hip hop music is characterized by rhythmic and rhyming speech (rapping) over beats created by DJs or producers. It often includes sampling from other songs, strong bass lines, and percussive elements.',
  'dance': 'It is a genre designed to get people moving on the dance floor. It typically features electronic music, synthesized melodies, and a strong bassline. Originating in clubs and underground scenes, it encompasses various subgenres like house, techno, and EDM, uniting people through rhythm and euphoria.',
  'bollywood': 'Bollywood music is the vibrant soundtrack of Indian cinema. It blends traditional Indian melodies with Western influences, incorporating elements of classical, folk, and contemporary music. Known for its catchy tunes, colorful visuals, and expressive lyrics.',
  'rock': 'Rock and metal music are powerful genres characterized by amplified instrumentation, distorted guitars, and aggressive vocals. Rock spans diverse styles from classic to alternative, often focusing on themes of rebellion, love, and social commentary.',
  'classical' : 'Classical music is a genre rooted in tradition, characterized by intricate compositions, orchestral arrangements, and timeless melodies. Acoustic musical instruments are generally used.'
}


const marks = [
  {
    value: 2,
    label: '2 Mins',
  },
  {
    value: 3,
    label: '3 Mins',
  },
  {
    value: 4,
    label: '4 Mins',
  },
  {
    value: 5,
    label: '5 Mins',
  },
  {
    value: 6,
    label: '6 Mins',
  },
  {
    value: 7,
    label: '7 Mins',
  }
];


function App() {
  const [open, setOpen] = useState(false);
  const [predicting, setPredicting] = useState(false);
  const [danceability, setDanceability] = useState(50);
  const [energy, setEnergy] = useState(50);
  const [acousticness, setAcousticness] = useState(50);
  const [speechiness, setSpeechiness] = useState(50);
  const [instrumentalness, setInstrumentalness] = useState(50);
  const [valence, setValence] = useState(50);
  const [tempo, setTempo] = useState(120);
  const [duration_ms, setDuration] = useState(4);
  const [genre, setPredictedGenre] = useState(null);

async function handlePredictGenre(){
    const params = {
      danceability: (danceability / 100).toFixed(2),
      energy: (energy / 100).toFixed(2),
      acousticness: (acousticness / 100).toFixed(2),
      speechiness: (speechiness / 400).toFixed(2),
      instrumentalness: (instrumentalness / 100).toFixed(2),
      tempo: (tempo),
      valence: (valence / 100).toFixed(2),
      duration: (duration_ms * 60000),  
    };
    try{
        setOpen(true);
        setPredicting(true);
        const response = await axios.get('https://genrepredictionapp.onrender.com/predict/', { params })
        setPredictedGenre(response.data.genre);  
        setPredicting(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setPredicting(false);
      }
  }
  


  return (
    <div className="App">
      <b><h1 id="heading">What's Your Taste in Music?</h1></b>
      <h2 id="secondHeading">Answer the simple questions below and get a music genre predicted according to your choices!</h2>
      <div className="questionsDiv">
        <h3 className="questions">How much do you enjoy dancing while listening to music?</h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={50}
            // getAriaValueText={valueText}
            step={1}
            value={danceability}
            onChange={(event, newValue) => setDanceability(newValue)}
            // marks={[{ value: 0, label: "I don't like to dance"}, { value: 100, label: "I can't go without dancing"}]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">How much energy do you prefer in your music?</h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={50}
            value={energy}
            onChange={(event, newValue) => setEnergy(newValue)}
            step={1}
            // marks={[{ value: 0, label: "Calm and Relaxing"}, { value: 100, label: "Intense and Energetic"}]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">How much do you enjoy music with acoustic instruments like guitars and pianos over electronic music?</h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={50}
            // getAriaValueText={valueText}
            value={acousticness}
            onChange={(event, newValue) => setAcousticness(newValue)}
            step={1}
            // marks={[{ value: 0, label: "I prefer electronic music"}, { value: 100, label: "Acoustic music is better"}]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">How important are lyrics and vocal elements in music to you?</h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={50}
            // getAriaValueText={valueText}
            value={speechiness}
            onChange={(event, newValue) => setSpeechiness(newValue)}
            step={1}
            // marks={[{ value: 0, label: "Who pays attention to lyrics?"}, { value: 100, label: "I listen to music only for the lyrics"}]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">How much emphasis do you give to the instrumentals and mid-tones of a song? </h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={50}
            // getAriaValueText={valueText}
            value={instrumentalness}
            onChange={(event, newValue) => setInstrumentalness(newValue)}
            step={1}
            // marks={[{ value: 0, label: "What are midtones? I'm a Basshead"}, { value: 100, label: "Instrumentalness is important to me"}]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">When it comes to music, how happy and uplifting do you prefer the sound to be, over melancholic music? </h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={50}
            // getAriaValueText={valueText}
            value={valence}
            onChange={(event, newValue) => setValence(newValue)}
            step={1}
            // marks={[{ value: 0, label: "I like melancholic music"}, { value: 100, label: "Isn't there enough sorrow in life?"}]}
            min={0}
            max={100}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">How fast do you prefer the tempo of your music to be?</h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Small steps"
            defaultValue={120}
            // getAriaValueText={valueText}
            value={tempo}
            onChange={(event, newValue) => setTempo(newValue)}
            step={20}
            marks={[{ value: 80, label: "Very Slow"}, { value: 100, label: "Slow"},{ value: 120, label: "Moderately Paced"}, { value: 140, label: "Fast"},{ value: 160, label: "Very Fast"}]}
            min={80}
            max={160}
            valueLabelDisplay="auto"
          />
        </Box>
        <h3 className="questions">For you, what is the ideal length of any song?</h3>
        <Box sx={{ width: 500 }}>
          <Slider
            aria-label="Custom marks"
            defaultValue={4}
            // getAriaValueText={valueText}
            value={duration_ms}
            onChange={(event, newValue) => setDuration(newValue)}
            step={1}
            marks={marks}
            min={2}
            max={7}
            valueLabelDisplay="auto"
          />
        </Box>
      </div>
      <Button id="submitButton" size="lg" onClick={handlePredictGenre}>Let's Go!</Button>
      <Modal id="modal"
        aria-labelledby="modal-title"
        aria-describedby="modal-desc"
        open={open}
        onClose={() => setOpen(false)}
        sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}
      >
        <Sheet
          variant="outlined"
          sx={{
            maxWidth: 500,
            borderRadius: 'md',
            p: 3,
            boxShadow: 'lg',
          }}
        >
          <ModalClose variant="plain" sx={{ m: 1 }} />
          {predicting?<Typography id="modal-title"> Predicting... <CircularProgress size='md' id='gola' /></Typography>:<Typography id="modal-title"> Prediction Complete!</Typography>}
          {predicting?<Typography id="modal-desc" textColor="text.tertiary">
           Do not click anywhere outside this popup. This may take a while if you're doing this for the first time, but the result will show up (eventually). Sorry but I can't afford to pay for a faster backend :P.
          </Typography>:<Typography id="modal-desc" textColor="text.tertiary">
            The genre that suits you the most is : <b>{output[genre]}</b>
          </Typography>}
          {predicting?null:<Typography id="modal-desc-s" textColor="text.tertiary">
            {desc[genre]}
          </Typography>}
        </Sheet>
      </Modal>

      {/* {genre && <h3>Your predicted genre is: {genre}</h3>} */}
    </div>
  );
}

export default App;
