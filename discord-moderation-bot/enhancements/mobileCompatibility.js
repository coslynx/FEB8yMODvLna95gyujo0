const mobileCompatibility = {
  checkMobileDevice: () => {
    // Function to check if the device is a mobile device
    const userAgent = navigator.userAgent;
    const mobileDevices = ["Android", "iPhone", "iPad", "Windows Phone"];
    
    return mobileDevices.some(device => userAgent.includes(device));
  },
  
  handleMobileActions: () => {
    // Function to handle mobile-specific actions
    if (mobileCompatibility.checkMobileDevice()) {
      // Mobile-specific actions here
    } else {
      // Desktop-specific actions here
    }
  }
};

export default mobileCompatibility;