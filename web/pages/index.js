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
            <p>By Alexander Cai, Zaki Rangwala, Ayden Heal, and Aahil Samnani</p>
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

        {/* Feature 2 */}
        <article className="container box style1 left">
          <a href="#" className="image fit"><img src="/images/pic02.jpg" alt="" /></a>
          <div className="inner">
            <header>
              <h2>Mollis posuere<br />
						lectus lacus</h2>
            </header>
            <p>Rhoncus mattis egestas sed fusce sodales rutrum et etiam ullamcorper. Etiam egestas scelerisque ac duis magna lorem ipsum dolor.</p>
          </div>
        </article>

        <RegistrationForm />

        {/* Portfolio */}
        <article className="container box style2">
          <header>
            <h2>Magnis parturient</h2>
            <p>Justo phasellus et aenean dignissim<br />
					placerat cubilia purus lectus.</p>
          </header>
          <div className="inner gallery">
            <div className="row gtr-0">
              <div className="col-3 col-12-mobile"><a href="/images/fulls/01.jpg" className="image fit"><img src="/images/thumbs/stocks.jpeg" alt="stocks" title="Stock market information" /></a></div>
              <div className="col-3 col-12-mobile"><a href="/images/fulls/02.jpg" className="image fit"><img src="/images/thumbs/weather.jpg" alt="" title="Dress prepared" /></a></div>
              <div className="col-3 col-12-mobile"><a href="/images/fulls/03.jpg" className="image fit"><img src="/images/thumbs/03.jpg" alt="" title="Raven" /></a></div>
              <div className="col-3 col-12-mobile"><a href="/images/fulls/04.jpg" className="image fit"><img src="/images/thumbs/04.jpg" alt="" title="I'll have a cup of Disneyland, please" /></a></div>
            </div>
            <div className="row gtr-0">
              <div className="col-3 col-12-mobile"><a href="/images/fulls/05.jpg" className="image fit"><img src="/images/thumbs/05.jpg" alt="" title="Cherish" /></a></div>
              <div className="col-3 col-12-mobile"><a href="/images/fulls/06.jpg" className="image fit"><img src="/images/thumbs/06.jpg" alt="" title="Different." /></a></div>
              <div className="col-3 col-12-mobile"><a href="/images/fulls/07.jpg" className="image fit"><img src="/images/thumbs/07.jpg" alt="" title="History was made here" /></a></div>
              <div className="col-3 col-12-mobile"><a href="/images/fulls/08.jpg" className="image fit"><img src="/images/thumbs/08.jpg" alt="" title="People come and go and walk away" /></a></div>
            </div>
          </div>
        </article>

        {/* Contact */}
        <article className="container box style3">
          <header>
            <h2>Nisl sed ultricies</h2>
            <p>Diam dignissim lectus eu ornare volutpat orci.</p>
          </header>
          <form method="post" action="#">
            <div className="row gtr-50">
              <div className="col-6 col-12-mobile"><input type="text" className="text" name="name" placeholder="Name" /></div>
              <div className="col-6 col-12-mobile"><input type="text" className="text" name="email" placeholder="Email" /></div>
              <div className="col-12">
                <textarea name="message" placeholder="Message"></textarea>
              </div>
              <div className="col-12">
                <ul className="actions">
                  <li><input type="submit" value="Send Message" /></li>
                </ul>
              </div>
            </div>
          </form>
        </article>

        <section id="footer">
          <ul className="icons">
            <li><a href="#" className="icon brands fa-twitter"><span className="label">Twitter</span></a></li>
            <li><a href="#" className="icon brands fa-facebook-f"><span className="label">Facebook</span></a></li>
            <li><a href="#" className="icon brands fa-google-plus-g"><span className="label">Google+</span></a></li>
            <li><a href="#" className="icon brands fa-pinterest"><span className="label">Pinterest</span></a></li>
            <li><a href="#" className="icon brands fa-dribbble"><span className="label">Dribbble</span></a></li>
            <li><a href="#" className="icon brands fa-linkedin-in"><span className="label">LinkedIn</span></a></li>
          </ul>
          <p>
            A brand new site template designed by <a href="http://twitter.com/ajlkn">AJ</a> for <a href="http://html5up.net">HTML5 UP</a>.<br />
            It’s responsive, built on HTML5/CSS3, and entirely free<br />
            under the <a href="http://html5up.net/license">Creative Commons license</a>.
          </p>
          <div className="copyright">
            <ul className="menu">
              <li>&copy; Alexander Cai, Zaki Rangwala, Ayden Heal, Aahil . All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
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
