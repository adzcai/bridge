import Head from 'next/head'
import RegistrationForm from '../components/registration-form';

// Based on Overflow by HTML5 UP
// html5up.net | @ajlkn
// Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

export default function Home() {
  return (
    <div>
      <Head>
        <title>Bridge</title>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <noscript><link rel="stylesheet" href="/assets/css/noscript.css" /></noscript>
      </Head>

      <div className="is-preload">

        {/* Header */}
        <section id="header">
          <header>
            <h1>Bridge</h1>
            <p>By Alex Cai, Zaki Rangwala, and Ayden Heal</p>
          </header>
          <footer>
            <a href="#banner" className="button style2 scrolly-middle">Push the frontier</a>
          </footer>
        </section>

        {/* Banner */}
        <section id="banner">
          <header>
            <h2>With you wherever you go</h2>
          </header>
          <p>With Bridge, you aren't limited by your data plan. As long as you have phone service, send a text to Bridget, an intelligent text assistant, to get the data you need.</p>
          <footer>
            <a href="#first" className="button style2 scrolly">Work worry-free</a>
          </footer>
        </section>

        {/* Feature 1 */}
        <article id="first" className="container box style1 right">
          <a href="#" className="image fit"><img src="/images/pic01.jpg" alt="" /></a>
          <div className="inner">
            <header>
              <h2>Powered by Twilio and APIs</h2>
            </header>
            <p>We connect with official APIs to deliver you instant and up-to-date information.</p>
          </div>
        </article>

        <RegistrationForm />

        {/* Portfolio */}
        <article className="container box style2">
          <header>
            <h2>Features and APIs</h2>
            <p>Justo phasellus et aenean dignissim<br />
					placerat cubilia purus lectus.</p>
          </header>
          <div className="inner gallery">
            <div className="row gtr-0">
              <div className="col-3 col-12-mobile thumb"><a href="/images/fulls/stocks.jpeg" className="image fit"><img src="/images/thumbs/stocks.jpeg" alt="stocks" title="Stock market information" /></a></div>
              <div className="col-3 col-12-mobile thumb"><a href="/images/fulls/weather.jpg" className="image fit"><img src="/images/thumbs/weather.jpg" alt="" title="Dress prepared" /></a></div>
              <div className="col-3 col-12-mobile thumb"><a href="/images/fulls/email.jpg" className="image fit"><img src="/images/thumbs/email.jpg" alt="" title="Raven" /></a></div>
              <div className="col-3 col-12-mobile thumb"><a href="/images/fulls/04.jpg" className="image fit"><img src="/images/thumbs/04.jpg" alt="" title="I'll have a cup of Disneyland, please" /></a></div>
            </div>
          </div>
        </article>

        <section id="footer">
          <div className="copyright">
            <ul className="menu">
              <li>&copy; January 2021 Alexander Cai, Zaki Rangwala, Ayden Heal. All rights reserved.</li><li>Design based on <a href="http://html5up.net">HTML5 UP</a>, a site template provided under the <a href="http://html5up.net/license">Creative Commons license</a>. by <a href="http://twitter.com/ajlkn">AJ</a></li>
            </ul>
          </div>
        </section>
      </div>

      <script src="/assets/js/jquery.min.js"></script>
      <script src="/assets/js/jquery.scrolly.min.js"></script>
      <script src="/assets/js/jquery.poptrox.min.js"></script>
      <script src="/assets/js/browser.min.js"></script>
      <script src="/assets/js/breakpoints.min.js"></script>
      <script src="/assets/js/util.js"></script>
      <script src="/assets/js/main.js"></script>
    </div>
  )
}
