import { useState } from "react";
import dynamic from 'next/dynamic';
import Head from 'next/head'
import styles from '../styles/Home.module.css'
import axios from "axios";

const Graphviz = dynamic(() => import('graphviz-react'), { ssr: false });

export default function Home() {
    const [file, setFile] = useState();
    const [dot, setDot] = useState('')

    const handleOnChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleOnSubmit = async (e) => {
        e.preventDefault();

        if (file) {
            const data = new FormData()
            data.append('file', file)

            const res = await axios.post('http://0.0.0.0:8088/generate_graph/', data, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            })

            if (!res.data) {
                console.error('ERROR')
            }

            if (typeof res.data.data === 'string') {
                const d = res.data.data.replace("\\", "")
                setDot(d)
            }
        }
    };

  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>

          <form>
              <input
                  type="file"
                  accept={".csv"}
                  onChange={handleOnChange}
              />
              <button type="submit" onClick={handleOnSubmit}>GET GRAPH</button>
          </form>

          {dot && <Graphviz dot={dot} />}
      </main>
    </div>
  )
}
