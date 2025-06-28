
import { Shield, Sparkles } from "lucide-react";

const Header = () => {
  return (
    <div className="relative overflow-hidden bg-gradient-to-br from-emerald-900 via-teal-800 to-cyan-900 text-white">
      <div className="absolute inset-0 bg-black/30" />
      <div className="absolute inset-0 bg-gradient-to-r from-emerald-600/20 to-cyan-600/20" />
      
      <div className="relative container mx-auto px-6 py-20 text-center">
        <div className="flex items-center justify-center gap-4 mb-8">
          <div className="p-4 bg-white/15 rounded-2xl backdrop-blur-md border border-white/20">
            <Shield className="h-10 w-10" />
          </div>
          <h1 className="text-5xl md:text-6xl font-extrabold bg-gradient-to-r from-white via-emerald-100 to-cyan-100 bg-clip-text text-transparent">
            Insurance AI Hub
          </h1>
        </div>
        
        <p className="text-2xl md:text-3xl font-medium mb-6 text-emerald-100 leading-relaxed">
          Next-generation AI suite for intelligent underwriting & risk management
        </p>
        
        <div className="flex items-center justify-center gap-3 text-cyan-300">
          <Sparkles className="h-6 w-6" />
          <span className="text-lg font-semibold">Enhanced by Machine Learning Intelligence</span>
        </div>
      </div>
      
      {/* Enhanced decorative elements */}
      <div className="absolute top-16 left-16 w-24 h-24 bg-emerald-400/10 rounded-full blur-2xl" />
      <div className="absolute bottom-12 right-16 w-40 h-40 bg-cyan-400/15 rounded-full blur-3xl" />
      <div className="absolute top-32 right-32 w-16 h-16 bg-white/10 rounded-full blur-xl" />
    </div>
  );
};

export default Header;
