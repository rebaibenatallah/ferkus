
/*=============== SHOW SIDEBAR ===============*/
const showSidebar = (toggleId, sidebarId, headerId, mainId) =>{
    const toggle = document.getElementById(toggleId),
          sidebar = document.getElementById(sidebarId),
          header = document.getElementById(headerId),
          main = document.getElementById(mainId)
 
    if(toggle && sidebar && header && main){
        toggle.addEventListener('click', ()=>{
            /* Show sidebar */
            sidebar.classList.toggle('show-sidebar')
            /* Add padding header */
            header.classList.toggle('left-pd')
            /* Add padding main */
            main.classList.toggle('left-pd')
        })
    }
 }
 showSidebar('header-toggle','sidebar', 'header', 'main')
 
 /*=============== LINK ACTIVE ===============*/
//  const sidebarLink = document.querySelectorAll('.sidebar__list a')
 
//  function linkColor(){
//      sidebarLink.forEach(l => l.classList.remove('active-link'))
//      this.classList.add('active-link')
//  }
 
//  sidebarLink.forEach(l => l.addEventListener('click', linkColor))
 
 /*=============== DARK LIGHT THEME ===============*/ 
 const themeButton = document.getElementById('theme-button')
 const logo1 = document.getElementById('logo1')
 const logo2 = document.getElementById('logo2')

 const darkTheme = 'dark-theme'
 const iconTheme = 'ri-sun-fill'
 
 // Previously selected topic (if user selected)
 const selectedTheme = localStorage.getItem('selected-theme')
 const selectedIcon = localStorage.getItem('selected-icon')
 
 // We obtain the current theme that the interface has by validating the dark-theme class
 const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
 const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'ri-moon-clear-fill' : 'ri-sun-fill'
 
 // We validate if the user previously chose a topic
 if (selectedTheme) {
   // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
   document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
   themeButton.classList[selectedIcon === 'ri-moon-clear-fill' ? 'add' : 'remove'](iconTheme)
}
 
 // Activate / deactivate the theme manually with the button
 themeButton.addEventListener('click', () => {
    let s = document.getElementById('logo1').src;
     // Add or remove the dark / icon theme
     document.body.classList.toggle(darkTheme)
     themeButton.classList.toggle(iconTheme)
     // We save the theme and the current icon that the user chose
     localStorage.setItem('selected-theme', getCurrentTheme())
     localStorage.setItem('selected-icon', getCurrentIcon())
    //  console.log(s.includes("img/1.png"))
     console.log(document.body.classList.contains(darkTheme))
     logo_theme()
 })
function logo_theme(){

    if( document.body.classList.contains(darkTheme) ){
        logo1.src= logo_n1;
        logo2.src= logo_n2;
    }else{
        logo1.src= logo_1;
        logo2.src= logo_2;
    }
}

logo_theme()
 